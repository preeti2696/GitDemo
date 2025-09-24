checkout_confirmation = shop_page.goToCart()
checkout_confirmation.checkout()
checkout_confirmation.enter_delivery_address("ind")
checkout_confirmation.validate_order()