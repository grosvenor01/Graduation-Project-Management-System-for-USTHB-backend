import usthb from '../assets/images/usthb.png';
import React from 'react';
function NavBar(){
    return (
        <nav className="navbar">
            <img src={usthb} alt="" />
            <ul>
                <li><a href="/home" class="underline-hover-effect">Home</a></li>
                <li><a href="/studentprofile" class="underline-hover-effect">Profile</a></li>
                <li><a href="#" class="underline-hover-effect">About</a></li>
                <li><a href="#" class="underline-hover-effect">Contact</a></li>
            </ul>
            <button><a href="/registration">s'inscrire</a></button>
        </nav>
    )
}

export default NavBar
