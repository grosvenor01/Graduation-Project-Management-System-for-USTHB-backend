import LoginLeft from "../../components/loginLeft"
import usthb from '../../assets/images/usthb.png';
import './login.css'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faAt,  faLock } from '@fortawesome/free-solid-svg-icons'
import { useState } from "react";
import {useNavigate} from 'react-router-dom'
import React from 'react';
function Login() {

    const [infos, setInfos]= useState({
        username: "",
        password: ""
    })

    const handleChange = (e) =>{
        const {name, value }=e.target
        setInfos ((prev)=>{
            return {...prev, [name]: value}
        })
    }

    const history = useNavigate()

    const handleSubmit = async(e) => {
        e.preventDefault();
        console.log(infos);
        const response = await fetch("http://localhost:8000/api/login/",{
            method: "POST",
            credentials:'include',
            headers: {
                'Content-Type' : 'application/json'
            },
            body: JSON.stringify(infos)
        })
        const result = await response.json();
        history("/home")
    }

    return(
        <div className="login registration">
            <div>
               <LoginLeft/>
            </div>
            <form action="" onSubmit={handleSubmit}>
              <img className="imgreg" src={usthb} alt="" />
              <h1 className="loginh">se connecter</h1>
              <p className="loginp">connectez vous ici pour plus d’accesbilité a notre platforme</p>

                <h3 className="head">Email </h3>
                <div className="box">
                <FontAwesomeIcon  icon={faAt} className="izan" />
                <input type="text" placeholder="username " className="test" name="username" onChange={handleChange}/>
                </div>
                
                <h3>Password </h3>
                <div className="box">
                <FontAwesomeIcon icon={faLock } className="izan"/>
                <input type="password" placeholder="*****************" className="test" name="password" onChange={handleChange}/>
                </div>

                <div className="checklogin">
                    <label htmlFor="">
                    <input type="checkbox" />
                    rappel moi
                    </label>
                    <a href="">J’ai oublier mon mot de pass</a>
                </div>

                <button className="regbtn1 bttn">Connexion</button>
                <p className="lastp"><a href ="/registration">Inscrivez vous</a> si vous n'avez pas un compte </p>

            </form>
        </div>
    )
}

export default Login