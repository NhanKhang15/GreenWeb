import React, { useEffect, useState } from 'react';

export default function Product() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/api/products')
      .then(res => res.json())
      .then(data => {
        if (data.success) setProducts(data.products);
      })
      .catch(err => console.error('Lỗi lấy sản phẩm:', err));
  }, []);

  return (
    <ul>
      {products.map(product => (
        <li key={product.ID} style={{ marginBottom: 16 }}>
          <img src={product.Image} alt={product.Name} width={80} />
          <div><strong>{product.Name}</strong></div>
          <div>Price: {product.Price} ₫</div>
          <div>Discount: {product.Discount}%</div>
          <div>Place: {product.Place}</div>
          <a href={product.Link} target="_blank" rel="noreferrer">Detail →</a>
        </li>
      ))}
    </ul>
  );
} 