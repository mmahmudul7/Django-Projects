import { useCallback, useState } from 'react';
import authApiClient from '../services/auth-api-client';

const useCart = () => {
    // const [authToken] = useState(
    //     () => JSON.parse(localStorage.getItem('authTokens')).access
    // );
    const [cart, setCart] = useState(null);
    const [cartId, setCartId] = useState(() => localStorage.getItem('cartId'));

    // Create a new Cart
    const createOrGetCart = useCallback(async () => {
        try {
            const response = await authApiClient.post('/carts/');

            if (!cartId) {
                localStorage.setItem('cartId', response.data.id);
                setCartId(response.data.id);
            }

            setCart(response.data);
        } catch (error) {
            console.log(error);
        }
    }, [cartId]);

    // Add items to the cart
    const AddCartItems = useCallback(
        async (product_id, quantity) => {
            if (!cartId) await createOrGetCart();

            try {
                const response = await authApiClient.post(
                    `/carts/${cartId}/items/`,
                    { product_id, quantity }
                );

                return response.data;
            } catch (error) {
                console.log('Error adding Items', error);
            }
        },
        [cartId, createOrGetCart]
    );

    return { cart, createOrGetCart, AddCartItems };
};

export default useCart;
