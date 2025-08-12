import { useState } from 'react';
import { FaShoppingCart } from 'react-icons/fa';
import { FaCheck, FaMinus, FaPlus } from 'react-icons/fa6';

const AddToCartButton = ({ product }) => {
    const [quantity, setQuantity] = useState(1);
    const [isAdding, setIsAdding] = useState(false);
    const [isAdded, setIsAdded] = useState(false);

    const increaseQuantity = () => {
        if (quantity < product.stock) {
            setQuantity(quantity + 1);
        }
    };

    const decreaseQuantity = () => {
        if (quantity > 1) {
            setQuantity(quantity - 1);
        }
    };

    const AddToCart = () => {
        // Simulate API Call
        setIsAdding(true);
        setTimeout(() => {
            setIsAdding(false);
            setIsAdded(true);

            setTimeout(() => {
                setIsAdded(false);
            }, 2000);
        }, 1000);
    };

    return (
        <div className="space-y-4">
            <div className="join">
                <button
                    className="btn btn-outline join-item"
                    onClick={decreaseQuantity}
                    disabled={quantity <= 1}
                >
                    <FaMinus className="h-4 w-4" />
                </button>
                <input
                    type="number"
                    value={quantity}
                    min={1}
                    max={product.stock}
                    className="input inut-bordered join-item w-16 text-center [appearance:textfield] [&::-webkit-inner-spain-button]:appearance-none [&::-webkit-outer-spin-button]:appearance-none"
                />
                <button
                    className="btn btn-outline join-item"
                    onClick={increaseQuantity}
                    disabled={quantity >= product.stock}
                >
                    <FaPlus className="h-4 w-4" />
                </button>
            </div>

            <button
                className="btn btn-secondary w-full"
                onClick={AddToCart}
                disabled={isAdding || isAdded || product.stock == 0}
            >
                {isAdding ? (
                    <span className="flex items-center">
                        <span className="loading loading-spinner loading-sm mr-2"></span>
                        Adding ...
                    </span>
                ) : isAdded ? (
                    <span className="flex items-center">
                        <FaCheck className="mr-2 h-4 w-4" /> Added to Cart
                    </span>
                ) : (
                    <span className="flex items-center">
                        <FaShoppingCart className="mr-2 h-4 w-4" /> Add to Cart
                    </span>
                )}
            </button>
        </div>
    );
};

export default AddToCartButton;
