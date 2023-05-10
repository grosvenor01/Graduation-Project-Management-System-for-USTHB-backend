import LoginLeft from "../../components/loginLeft";
import './registration.css'
import google from '../../assets/images/google.png';
import usthb from '../../assets/images/usthb.png';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faEnvelope, faPenToSquare, faLock } from '@fortawesome/free-solid-svg-icons'
import { useState } from "react";
import {useNavigate} from 'react-router-dom'
import React from 'react';

function Registration(){

    const [details, setDetails]= useState({
        type: "",
        username: "",
        email: "",
        password: "",
    })

    const handleChange = (e) =>{
        const {name, value }=e.target
        setDetails ((prev)=>{
            return {...prev, [name]: value}
        })
    }

   const history = useNavigate()

    const handleSubmit = async (e) => {
        e.preventDefault();
        console.log(details);
        const response = await fetch("http://localhost:8000/api/register/",{
            method: "POST",
            headers: {
                'Content-Type' : 'application/json'
            },
            body: JSON.stringify(details)
        })
        const result = await response.json();
        console.log(result)
        history("/login")
    }


    return(
        <div className="registration">
           <div>
              <LoginLeft/>
           </div>
           <div className="regform">
            <img className="imgreg" src={usthb} alt="" />
            <h1>s'inscrire</h1>
            <p>inscriver vous ici pour plus d’accesbilité a notre platforme</p>
            <br />
            <br />
            <h3 className="vous">Vous etes un : </h3>
            <form action=""  onSubmit={handleSubmit} >
               <div className="radios">
                   <button className="radiobtn">
                      <label htmlFor="">
                      <input type="radio" name="type" onChange={handleChange}/>
                      Etudiant 
                      </label>
                   </button>
                   <button className="radiobtn">
                      <label htmlFor="">
                      <input type="radio" name="type" onChange={handleChange}/>
                      Ensignant
                      </label>
                    </button >
                    <button className="radiobtn">
                      <label htmlFor="">
                      <input type="radio" name="type" onChange={handleChange}/>
                      Entreprise 
                      </label>
                    </button>
               </div>

                <h3>Nom & Prenom </h3>
                <div className="box">
                <FontAwesomeIcon  icon={faPenToSquare} className="izan" />
                <input type="text" placeholder=" Full name " className="test" name="username" onChange={handleChange}/>
                </div>
                
                
                <h3>Email </h3>
                <div className="box">
                <FontAwesomeIcon icon={faEnvelope} className="izan"/>
                <input type="email" placeholder="username@gmail.com" className="test" name="email" onChange={handleChange}/>
                </div>


                <h3>Password </h3>
                <div className="box" >
                <FontAwesomeIcon icon={faLock} className="izan"/>
                <input type="password"  placeholder="*****************"  className="test" name="password" onChange={handleChange}/>
                </div>
                
                <br />
                <br />
                <br />
                <br />
                <br />
                <br />
                <button className="regbtn1" >creer compte</button>
                <br />
                <br />
                <button className="regbtn2"> <img className="google" src={google} alt="" /> inscriver vous avec google</button>
                <p className="lastp"><a href="/login">Connectez vous</a> si vous avez deja un compte </p>
            </form>
            </div>
        </div>
    )

}

export default Registration