import OrderCard from '../components/Orders/OrderCard';

const Orders = () => {
    const orders = [
        {
            id: 'b941bd87-8bfa-4838-91c9-d11694826ab3',
            user: 3,
            status: 'Not Paid',
            total_price: 600.0,
            created_at: '2025-03-19T14:13:30.715441Z',
            items: [
                {
                    id: 9,
                    product: {
                        id: 1,
                        name: 'Smartphone',
                        price: 150.0,
                    },
                    price: 150,
                    quantity: 2,
                    total_price: 300.0,
                },
                {
                    id: 10,
                    product: {
                        id: 1,
                        name: 'Tablet',
                        price: 300.0,
                    },
                    price: 300.0,
                    quantity: 1,
                    total_price: 300.0,
                },
            ],
        },
    ];

    return (
        <div className="container mx-auto px-4 py-8">
            <h1 className="text-2xl font-bold mb-6">Order Details</h1>
            {orders.map((order) => (
                <OrderCard key={order.id} order={order} />
            ))}
        </div>
    );
};

export default Orders;
