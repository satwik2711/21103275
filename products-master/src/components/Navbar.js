import React from "react";
import { AppBar, Toolbar, Typography, Button } from "@mui/material";
import { Link as RouterLink } from "react-router-dom";

function NavBar() {
  return (
    <AppBar position="static" sx={{ flexGrow: 1 }}>
      <Toolbar>
        <Typography variant="h6" sx={{ flexGrow: 1 }}>
          Top N Products
        </Typography>
        <Button
          color="inherit"
          component={RouterLink}
          to="/allproducts"
          sx={{ color: "white", textDecoration: "none" }}
        >
          All Products
        </Button>
      </Toolbar>
    </AppBar>
  );
}

export default NavBar;
