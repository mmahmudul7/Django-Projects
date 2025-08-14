import { useState } from 'react';
import apiClient from '../services/api-client';

const useCart = () => {
    const [authToken, setAuthToken] = useState(
        () => JSON.parse(localStorage.getItem('authTokens')).access
    );
    const [cart, setCart] = useState(null);
    const [cartId, setCartId] = useState(() => localStorage.getItem('cartId'));
    // Create a new Cart
    const createOrGetCart = async () => {
        // console.log(authToken);
        try {
            const response = await apiClient.post(
                '/carts/',
                {},
                {
                    headers: { Authorization: `JWT ${authToken}` },
                }
            );
            // console.log(response.data);
            if (!cartId) {
                localStorage.setItem('cartId', response.data.id);
                setCartId(response.data.id);
            }
            setCart(response.data);
        } catch (error) {
            console.log(error);
        }
    };
    return { cart, createOrGetCart };
};

export default useCart;
