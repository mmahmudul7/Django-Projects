const List = () => {
    const fruits = ['Apple', 'Banana', 'Orange', 'Grapes', 'Mango', 'Pine Apple', 'Coconut'];

    return (
        <div>
            <ul>
                {fruits.map((fruit) => {
                    return <li key={fruit}>{fruit}</li>;
                })}
            </ul>
        </div>
    );
};

export default List;