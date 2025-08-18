import { Suspense, useEffect, useState } from 'react';
import useCartContext from '../hooks/useCartContext';
import CartItemList from '../components/Cart/CartItemList';
import CartSummary from '../components/Cart/CartSummary';

const Cart = () => {
    const {
        cart,
        loading,
        createOrGetCart,
        updateCartItemQuantity,
        deleteCartItems,
    } = useCartContext();

    const [localCart, setLocalCart] = useState(cart);

    useEffect(() => {
        console.log('Create or get');
        if (!cart && !loading) createOrGetCart();
    }, [createOrGetCart, cart, loading]);

    useEffect(() => {
        setLocalCart(cart);
    }, [cart]);

    const handleUpdateQuantity = async (itemId, newQuantity) => {
        const prevLocalCartCopy = localCart; // Store a copy of localCart

        setLocalCart((prevLocalCart) => ({
            ...prevLocalCart,
            items: prevLocalCart.items.map((item) =>
                item.id == itemId ? { ...item, quantity: newQuantity } : item
            ),
            total_price: prevLocalCart.items.reduce(
                (sum, item) => sum + item.total_price,
                0
            ),
        }));

        try {
            await updateCartItemQuantity(itemId, newQuantity);
        } catch (error) {
            console.log(error);
            setLocalCart(prevLocalCartCopy); // Rollback to previous state if API fails
        }
    };

    const handleRemoveItem = async (itemId) => {
        setLocalCart((prevLocalCart) => ({
            ...prevLocalCart,
            items: prevLocalCart.items.filter((item) => item.id != itemId),
        }));

        try {
            await deleteCartItems(itemId);
        } catch (error) {
            console.log(error);
        }
    };

    if (loading) return <p>Loading ....</p>;
    if (!localCart) return <p>No Cart Found</p>;

    return (
        <div className="container mx-auto px-4 py-8">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div>
                    <Suspense fallback={<p>Loading....</p>}>
                        <CartItemList
                            items={localCart.items}
                            handleUpdateQuantity={handleUpdateQuantity}
                            handleRemoveItem={handleRemoveItem}
                        />
                    </Suspense>
                </div>
                <div>
                    <CartSummary
                        totalPrice={localCart.total_price}
                        itemCount={localCart.items.length}
                    />
                </div>
            </div>
        </div>
    );
};

export default Cart;
