import React from 'react';
import logo from './logo.svg';
import './App.css';
import { useGetAllIngredients } from './hooks/useGetAllIngredients';
import { useGetAllRecipes } from './hooks/useGetAllRecipes';


export const API_BASE_URL = "http://localhost:5000"

function App() {


  const { allIngredients } = useGetAllIngredients()
  const { allRecipes } = useGetAllRecipes()

  const handleGetAllRecipes = () => {
    console.log(allRecipes)
  }

  const handleGetAllIngredients = () => {
    console.log(allIngredients)
  }



  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <div style={{}}>

          <button style={{ background: "#62dafb", height: "40px", width: "150px", cursor: "pointer", marginRight: "20px" }} onClick={handleGetAllRecipes}>Print All Recipes</button>
          <button style={{ background: "#62dafb", height: "40px", cursor: "pointer", width: "150px" }} onClick={handleGetAllIngredients}>Print All Ingredients</button>

        </div>
      </header>
    </div>
  );
}

export default App;
