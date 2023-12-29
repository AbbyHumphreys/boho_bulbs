let stripePublicKey = document.getElementById('id_stripe_public_key').textContent.slice(1, -1);
let clientSecret = document.getElementById('id_client_secret').textContent.slice(1, -1);

let stripe = Stripe(stripePublicKey);

  // Create an instance of Elements.
  let elements = stripe.elements();

  // create some style for the card element
  let style = {
    base: {
      color: '#32325d',
      lineHeight: '18px',
      fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
      fontSmoothing: 'antialiased',
      fontSize: '16px',
      '::placeholder': {
        color: '#aab7c4'
      }
    },
    invalid: {
      color: '#fa755a',
      iconColor: '#fa755a'
    }
  };

  // Create an instance of the card Element.
  let card = elements.create('card', {style: style});

  // Add an instance of the card Element into the `card-element` <div>.
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

// Handle form submission.
let form = document.getElementById('payment-form');


let successElement = document.getElementById('stripe-token-handler');
form.addEventListener('submit', function(event) {
  event.preventDefault();

  card.update({ 'disabled': true});
  document.getElementById('submit-button').disabled = true;

  toggleFade(document.getElementById('payment-form'));
  toggleFade(document.getElementById('loading-overlay'));

  stripe.confirmCardPayment(clientSecret, {
      payment_method: {
          card: card,
      }
  }).then(function(result) {
    if (result.error) {
      let errorElement = document.getElementById('card-errors');
      errorElement.textContent = result.error.message;
      toggleFade(document.getElementById('payment-form'));
      toggleFade(document.getElementById('loading-overlay'));
      card.update({ 'disabled': false});
      document.getElementById('submit-button').disabled = false;
    } else {
      if (result.paymentIntent.status === 'succeeded') {
        // Insert the token ID into the form so it gets submitted to the server
        let hiddenInput = document.createElement('input');
        hiddenInput.setAttribute('type', 'hidden');
        hiddenInput.setAttribute('name', 'stripeToken');
        hiddenInput.setAttribute('value', result.paymentIntent.id);
        form.appendChild(hiddenInput);
        form.submit();
      }
    }
  }).catch(function(error) {
    // Removes console error for promise
    console.error("Error during payment:", error);
});;
});

function stripeTokenHandler(token) {
  successElement.className = '';
  successElement.querySelector('.token').textContent = token.id;
  // Insert the token ID into the form so it gets submitted to the server
  let form = document.getElementById('payment-form');
  let hiddenInput = document.createElement('input');
  hiddenInput.setAttribute('type', 'hidden');
  hiddenInput.setAttribute('name', 'stripeToken');
  hiddenInput.setAttribute('value', token.id);
  form.appendChild(hiddenInput);

  // Submit the form
  form.submit();
}

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