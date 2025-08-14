import { Suspense, useEffect, useState } from 'react';
import useCartContext from '../hooks/useCartContext';
import CartItemList from '../components/Cart/CartItemList';

const Cart = () => {
    const { cart, loading, createOrGetCart, updateCartItemQuantity } =
        useCartContext();

    const [localCart, setLocalCart] = useState(cart);

    useEffect(() => {
        console.log('Create or get');
        if (!cart && !loading) createOrGetCart();
    }, [createOrGetCart, cart, loading]);

    useEffect(() => {
        setLocalCart(cart);
    }, [cart]);

    const handleUpdateQuantity = async (itemId, newQuantity) => {
        setLocalCart((prevLocalCart) => ({
            ...prevLocalCart,
            items: prevLocalCart.items.map((item) =>
                item.id == itemId ? { ...item, quantity: newQuantity } : item
            ),
        }));

        try {
            await updateCartItemQuantity(itemId, newQuantity);
        } catch (error) {
            console.log(error);
        }
    };

    if (loading) return <p>Loading ....</p>;
    if (!localCart) return <p>No Cart Found</p>;

    return (
        <div className="flex justify-between">
            <div>
                <Suspense fallback={<p>Loading....</p>}>
                    <CartItemList
                        items={localCart.items}
                        handleUpdateQuantity={handleUpdateQuantity}
                    />
                </Suspense>
            </div>
            <div></div>
        </div>
    );
};

export default Cart;
