import { useCallback, useState } from 'react';
import authApiClient from '../services/auth-api-client';

const useCart = () => {
    // const [authToken] = useState(
    //     () => JSON.parse(localStorage.getItem('authTokens')).access
    // );
    const [cart, setCart] = useState(null);
    const [cartId, setCartId] = useState(() => localStorage.getItem('cartId'));
    const [loading, setLoading] = useState(false);

    // Create a new Cart
    const createOrGetCart = useCallback(async () => {
        setLoading(true);
        try {
            const response = await authApiClient.post('/carts/');

            if (!cartId) {
                localStorage.setItem('cartId', response.data.id);
                setCartId(response.data.id);
            }

            setCart(response.data);
        } catch (error) {
            console.log(error);
        } finally {
            setLoading(false);
        }
    }, [cartId]);

    // Add items to the cart
    const AddCartItems = useCallback(
        async (product_id, quantity) => {
            if (!cartId) await createOrGetCart();
            setLoading(true);

            try {
                const response = await authApiClient.post(
                    `/carts/${cartId}/items/`,
                    { product_id, quantity }
                );

                return response.data;
            } catch (error) {
                console.log('Error adding Items', error);
            } finally {
                setLoading(false);
            }
        },
        [cartId, createOrGetCart]
    );

    // Update Item quantity
    const updateCartItemQuantity = useCallback(
        async (itemId, quantity) => {
            try {
                await authApiClient.patch(`/carts/${cartId}/items/${itemId}`, {
                    quantity,
                });
            } catch (error) {
                console.log('Error updating cart items', error);
            }
        },
        [cartId]
    );

    // Delete Cart Item
    const deleteCartItems = useCallback(
        async (itemId) => {
            try {
                await authApiClient.delete(`/carts/${cartId}/items/${itemId}/`);
            } catch (error) {
                console.log(error);
            }
        },
        [cartId]
    );

    return {
        cart,
        loading,
        createOrGetCart,
        AddCartItems,
        updateCartItemQuantity,
        deleteCartItems,
    };
};

export default useCart;
