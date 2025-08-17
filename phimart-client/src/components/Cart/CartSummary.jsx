const CartSummary = () => {
    return (
        <div className="card bg-base-100 shadow-2xl">
            <div className="card-body">
                <h2 className="text-xl font-semibold mb-4">Order Summary</h2>

                <div className="space-y-2">
                    <div className="flex justify-between">
                        <span className="text-gray-500">Subtotal 10 Items</span>
                    </div>
                </div>

                <div className="flex justify-between">
                    <span className="text-gray-500">Shipping</span>
                    <span>100</span>
                </div>

                <div className="flex justify-between">
                    <span className="text-gray-500">Estimated Tax</span>
                    <span>12</span>
                </div>

                <div className="border-t border-gray-200 pt-2 mt-2">
                    <div className="flex justify-between font-medium">
                        <span>Order Total</span>
                        <span>120</span>
                    </div>
                </div>

                <div className="card-actions justify-end mt-4">
                    <button className="btn btn-secondary w-full">
                        Process to Checkout
                    </button>
                </div>
            </div>
        </div>
    );
};

export default CartSummary;
