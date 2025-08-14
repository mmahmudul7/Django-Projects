import { useEffect } from 'react';
import useCartContext from '../hooks/useCartContext';

const Cart = () => {
    const { cart, createOrGetCart } = useCartContext();

    useEffect(() => {
        createOrGetCart();
    }, []);

    return (
        <div>
            This is cart page <br />
            <h2>{JSON.stringify(cart)}</h2>
        </div>
    );
};

export default Cart;
