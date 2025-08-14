import { useEffect } from 'react';
import useCartContext from '../hooks/useCartContext';
import CartItemList from '../components/Cart/CartItemList';

const Cart = () => {
    // const { cart, createOrGetCart } = useCartContext();
    const { createOrGetCart } = useCartContext();

    useEffect(() => {
        console.log('Create or get');
        createOrGetCart();
    }, [createOrGetCart]);

    return (
        <div>
            <div>
                <CartItemList />
            </div>
            <div></div>
        </div>
    );
};

export default Cart;
