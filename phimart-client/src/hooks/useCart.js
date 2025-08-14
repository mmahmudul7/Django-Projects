import { useState } from 'react';
import apiClient from '../services/api-client';

const useCart = () => {
    const [authToken, setAuthToken] = useState(
        () => JSON.parse(localStorage.getItem('authTokens')).access
    );
    const [cart, setCart] = useState(null);
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
            setCart(response.data);
            localStorage.setItem('cartId', response.data.id);
        } catch (error) {
            console.log(error);
        }
    };
    return { cart, createOrGetCart };
};

export default useCart;
