# Tivona_project
python version --- Python 3.9.6
Created 3 test case 
TC1--test_successful_login-->Login with valid credentials & verify the display of (any)product.
TC2--test_display_added_items-->Add a product to the cart and verify the display of the product name in the "YOUR CART"Page.
TC3--test_successful_logout-->As the application will be logged in (after TC2),click logout and login back.Logout again and verify the display of "login" button.


TC2 and TC3--Passed
TC1--gets assertion failure_When i use ts.MarkFinal-->Its not able to find the element in explicit wait,but in the next step same element is found.
TC1--gets Passed,if i use ts.mark

                                                
