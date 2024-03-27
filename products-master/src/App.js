import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import NavBar from './components/Navbar';
import AllProducts from './pages/AllProducts';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <NavBar />
        <Routes>
          <Route path="/allproducts" element={<AllProducts />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;