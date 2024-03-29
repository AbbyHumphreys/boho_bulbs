let stripePublicKey = document.getElementById('id_stripe_public_key').textContent.slice(1, -1);
let clientSecret = document.getElementById('id_client_secret').textContent.slice(1, -1);

let stripe = Stripe(stripePublicKey);

let elements = stripe.elements({clientSecret});

var style = {
  base: {
      color: '#000',
      fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
      fontSmoothing: 'antialiased',
      fontSize: '16px',
      '::placeholder': {
          color: '#aab7c4'
      }
  },
  invalid: {
      color: '#dc3545',
      iconColor: '#dc3545'
  }
};

let card = elements.create('card', {style: style});

card.mount('#card-element');

// Handle real-time validation errors from the card Element.
card.addEventListener('change', function(event) {
  let displayError = document.getElementById('card-errors');
  if (event.error) {
    displayError.textContent = event.error.message;
  } else {
    displayError.textContent = '';
  }
});

let form = document.getElementById('payment-form');

// Handle form submit event
form.addEventListener('submit', function(event) {
  event.preventDefault();
  card.update({ 'disabled': true});
  document.getElementById('submit-button').disabled = true;

  toggleFade(document.getElementById('payment-form'));
  toggleFade(document.getElementById('loading-overlay'));

  let csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
  let saveInfo = document.getElementById('id-save-info').checked;
  fetch('/checkout/cache_checkout_data/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-CSRFToken': csrfToken
    },
    body: `client_secret=${clientSecret}&save_info=${saveInfo}`
  })
  .then(response => {
    if (!response.ok) {
        throw new Error('Network response was not ok.');
    }
    
    return stripe.confirmCardPayment(clientSecret, {
      payment_method: {
        card: card,
        billing_details: {
          name: form.full_name.value.trim(),
          phone: form.phone_number.value.trim(),
          email: form.email.value.trim(),
          address: {
              line1: form.street_address1.value.trim(),
              line2: form.street_address2.value.trim(),
              city: form.town_or_city.value.trim(),
              country: form.country.value.trim(),
              postal_code: form.postcode.value.trim(),
              state: form.county.value.trim(),
          }
        }
      },
      shipping: {
        name: form.full_name.value.trim(),
        phone: form.phone_number.value.trim(),
        address: {
            line1: form.street_address1.value.trim(),
            line2: form.street_address2.value.trim(),
            city: form.town_or_city.value.trim(),
            country: form.country.value.trim(),
            postal_code: form.postcode.value.trim(),
            state: form.county.value.trim(),
        }
      }
    });
  })
  .then(function(result) {
    if (result.paymentIntent.status === 'succeeded') {
      // Insert the token ID into the form so it gets submitted to the server
      let hiddenInput = document.createElement('input');
      hiddenInput.setAttribute('type', 'hidden');
      hiddenInput.setAttribute('name', 'stripeToken');
      hiddenInput.setAttribute('value', result.paymentIntent.id);
      form.appendChild(hiddenInput);
      form.submit();
    }
  })
  .catch(function(error) {
    console.error("Error during payment:", error);
  });
});

// Overlay toggle
function toggleFade(element) {
  if (window.getComputedStyle(element).display === "none") {
      element.style.display = "block";
      // Fix: Ensure the element is rendered before changing opacity
      setTimeout(() => { element.style.opacity = 1; }, 10);
  } else {
      element.style.opacity = 0;
      // Wait for the transition to finish before hiding the element
      setTimeout(() => { element.style.display = "none"; }, 1000);
  }
}