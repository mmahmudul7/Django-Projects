import { FaShoppingCart } from 'react-icons/fa';
import { FaMinus, FaPlus } from 'react-icons/fa6';

const AddToCartButton = () => {
    return (
        <div>
            <div className="join">
                <button className="btn btn-outline join-item">
                    <FaMinus className="h-4 w-4" />
                </button>
                <input
                    type="number"
                    min={1}
                    className="input inut-bordered join-item w-16 text-center [appearance:textfield] [&::-webkit-inner-spain-button]:appearance-none [&::-webkit-outer-spin-button]:appearance-none"
                />
                <button className="btn btn-outline join-item">
                    <FaPlus className="h-4 w-4" />
                </button>
            </div>

            <button className="btn btn-secondary w-full">
                <span className="flex items-center">
                    <FaShoppingCart className="mr-2 h-4 w-4" /> Add to Cart
                </span>
            </button>
        </div>
    );
};

export default AddToCartButton;
