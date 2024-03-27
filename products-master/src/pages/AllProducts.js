import React, { useEffect, useState } from "react";
import axios from "axios";
import {
  Grid,
  Typography,
  CircularProgress,
  Select,
  MenuItem,
} from "@mui/material";

const AllProducts = () => {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selectedCategory, setSelectedCategory] = useState("Phone");
  const [selectedCompany, setSelectedCompany] = useState("AMZ");

  const handleCategorySelect = (event) => {
    setSelectedCategory(event.target.value);
  };

  const handleCompanySelect = (event) => {
    setSelectedCompany(event.target.value);
  };

  useEffect(() => {
    const options = {
      method: "GET",
      url: `/test/companies/${selectedCompany}/categories/${selectedCategory}/products`,
      params: { top: "10", minPrice: "1", maxPrice: "10000" },
      headers: {
        Authorization:
          "Bearer token_here",
      },
    };

    axios
      .request(options)
      .then(function (response) {
        console.log(response.data);
        setProducts(response.data);
        setLoading(false);
      })
      .catch(function (error) {
        console.error(error);
      });
  }, [selectedCategory, selectedCompany]);

  if (loading) {
    return <CircularProgress />;
  }

  return (
    <div>
      <div>
        <Select value={selectedCompany} onChange={handleCompanySelect}>
          <MenuItem value={"AMZ"}>AMZ</MenuItem>
          <MenuItem value={"FLP"}>FLP</MenuItem>
          <MenuItem value={"SNP"}>SNP</MenuItem>
          <MenuItem value={"MYN"}>MYN</MenuItem>
          <MenuItem value={"AZO"}>AZO</MenuItem>
        </Select>
        <Select value={selectedCategory} onChange={handleCategorySelect}>
          <MenuItem value={"Phone"}>Phone</MenuItem>
          <MenuItem value={"Computer"}>Computer</MenuItem>
          <MenuItem value={"TV"}>TV</MenuItem>
          <MenuItem value={"Earphone"}>Earphone</MenuItem>
          <MenuItem value={"Tablet"}>Tablet</MenuItem>
          <MenuItem value={"Charger"}>Charger</MenuItem>
          <MenuItem value={"Mouse"}>Mouse</MenuItem>
          <MenuItem value={"Keypad"}>Keypad</MenuItem>
          <MenuItem value={"Bluetooth"}>Bluetooth</MenuItem>
          <MenuItem value={"Pendrive"}>Pendrive</MenuItem>
          <MenuItem value={"Remote"}>Remote</MenuItem>
          <MenuItem value={"Speaker"}>Speaker</MenuItem>
          <MenuItem value={"Headset"}>Headset</MenuItem>
          <MenuItem value={"Laptop"}>Laptop</MenuItem>
          <MenuItem value={"PC"}>PC</MenuItem>
        </Select>
      </div>
      <Grid container spacing={2}>
        {products.map((product, index) => (
          <Grid item xs={3} md={2} key={index}>
            <Typography variant="h4">{product.productName}</Typography>
            <Typography variant="subtitle1">Price: {product.price}</Typography>
            <Typography variant="subtitle1">
              Rating: {product.rating}
            </Typography>
            <Typography variant="subtitle1">
              Discount: {product.discount}
            </Typography>
            <Typography variant="subtitle1">
              Availability: {product.availability}
            </Typography>
          </Grid>
        ))}
      </Grid>
    </div>
  );
};

export default AllProducts;
