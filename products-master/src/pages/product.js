import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { Typography, Grid, CircularProgress } from '@mui/material';
import axios from 'axios';

const Product = () => {
    const { productId } = useParams();
    const [product, setProduct] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchProduct = async () => {
            try {
                const response = await axios.get(`/api/products/${productId}`);
                setProduct(response.data);
                setLoading(false);
            } catch (error) {
                console.error(error);
            }
        };

        fetchProduct();
    }, [productId]);

    if (loading) {
        return <CircularProgress />;
    }

    if (!product) {
        return <Typography variant="h6">Product not found</Typography>;
    }

    return (
        <Grid container spacing={2}>
            <Grid item xs={12}>
                <Typography variant="h4">{product.name}</Typography>
            </Grid>
            <Grid item xs={12}>
                <Typography variant="subtitle1">Company: {product.company}</Typography>
            </Grid>
            <Grid item xs={12}>
                <Typography variant="subtitle1">Category: {product.category}</Typography>
            </Grid>
            <Grid item xs={12}>
                <Typography variant="subtitle1">Price: {product.price}</Typography>
            </Grid>
            <Grid item xs={12}>
                <Typography variant="subtitle1">Rating: {product.rating}</Typography>
            </Grid>
            <Grid item xs={12}>
                <Typography variant="subtitle1">Discount: {product.discount}</Typography>
            </Grid>
            <Grid item xs={12}>
                <Typography variant="subtitle1">Availability: {product.availability}</Typography>
            </Grid>
        </Grid>
    );
};

export default Product;
