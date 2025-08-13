import { useEffect } from 'react';
import useCartContext from '../hooks/useCartContext';

const Cart = () => {
    const { createCart } = useCartContext();

    useEffect(() => {
        createCart();
    }, []);

    return <div>This is cart page</div>;
};

export default Cart;
