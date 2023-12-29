let stripePublicKey = document.getElementById('id_stripe_public_key').textContent.slice(1, -1);

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
form.addEventListener('submit', function(event) {
  event.preventDefault();

  // Disable the card and the submit button
  card.update({ 'disabled': true});
  document.getElementById('submit-button').disabled = true;

  stripe.confirmCardPayment(clientSecret, {
      payment_method: {
          card: card,
      }
  })
  stripe.createToken(card).then(function(result) {
    if (result.error) {
      // Inform the user if there was an error.
      let errorElement = document.getElementById('card-errors');
      errorElement.textContent = result.error.message;
      // Re-enable the card and the submit button
      card.update({ 'disabled': false});
      document.getElementById('submit-button').disabled = false;
    } else {
        if (result.paymentIntent.status === 'succeeded') {
            // Submit the form
            form.submit();
        }
  }});
});

let successElement = document.getElementById('stripe-token-handler');

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