import { FaRegTrashAlt } from 'react-icons/fa';

const CartItemList = () => {
    return (
        <div className="space-y-4">
            <h2 className="text-xl font-semibold">Shopping Cart</h2>

            <div className=" overflow-x-auto">
                <table className="table w-full">
                    <thead>
                        <tr>
                            <th>Product</th>
                            <th className="text-right">Price</th>
                            <th>Quanity</th>
                            <th className="text-right">Total</th>
                            <th></th>
                        </tr>
                    </thead>

                    <tbody>
                        <tr>
                            <td className="font-medium">Mystery Novel</td>
                            <td className="text-right">$100.00</td>
                            <td>
                                <div className="flex items-center join">
                                    <button className="btn btn-xs btn-outline join-item">
                                        -
                                    </button>
                                    <input
                                        type="number"
                                        min="1"
                                        className="input input-xs input-bordered join-item w-12 text-center [appearance:textfield] [&::-webkit-outer-spin-button]:appearance-none [&::-webkit-inner-spin-button]:appearance-none"
                                    />
                                    <button className="btn btn-xs btn-outline join-item">
                                        +
                                    </button>
                                </div>
                            </td>
                            <td className="text-right font-medium">$116.00</td>
                            <td>
                                <button className="btn btn-ghost btn-xs btn-circle">
                                    <FaRegTrashAlt className="h-4 w-4" />{' '}
                                </button>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    );
};

export default CartItemList;
