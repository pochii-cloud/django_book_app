// var stripe = Stripe('pk_test_51JDs2IBE8G6viZE98DrYyqQnEkQbyS5JXuAn1qyTIvxqe4YxMfRMPaGSb9FAyGbPJx0n2wQFIWRoVxZP7IhnFDZM00WvleIfex');
// Book App  
var stripe = Stripe('pk_test_51JUIwgARRlrXWO139iDgMqjL1tdbohUfNa4KSXvKq7tpFcg8PmY9X4hmanbvOwiJGhOAEq9tL6CExFyf1vpsyyGm00h5J5gCb5');

var checkoutButton = document.getElementById('checkout-button');

checkoutButton.addEventListener('click', function() {
    console.log("inner")
  stripe.redirectToCheckout({
    // Make the id field from the Checkout Session creation API response
    // available to this file, so you can provide it as argument here
    // instead of the {{CHECKOUT_SESSION_ID}} placeholder.
    sessionId: sessionid
  }).then(function (result) {
    // If `redirectToCheckout` fails due to a browser or network
    // error, display the localized error message to your customer
    // using `result.error.message`.
  });
});