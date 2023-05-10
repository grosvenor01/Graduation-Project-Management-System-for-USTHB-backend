import NavBar from "../../components/navbar";
import Header from "../../components/header";
import Info from "../../components/info";
import Photos from "../../components/photos";
import Numbers from "../../components/numbers";
import Footer from "../../components/footer";
import './main.css'
import React from 'react';

function Main() {
    return (
      <div className="main">
        <NavBar/>
        <Header/>
        <Info/>
        <Photos/>
        <Numbers/>
        <Footer/>
      </div>
    );
}

export default Main 