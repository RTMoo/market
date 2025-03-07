const ProductList = ({ products }) => {
    return (
        <div>
            {products.map((product) => (
                <div key={product.id} style={{ border: "1px solid #ccc", padding: "10px", marginBottom: "10px" }}>
                    <h3>{product.title}</h3>
                    <p>Цена: {product.price} руб.</p>
                    <p>В наличии: {product.stock} шт.</p>
                </div>
            ))}
        </div>
    );
};

export default ProductList;