import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faXmark } from '@fortawesome/free-solid-svg-icons'
import { useState } from 'react'
import React from 'react';
function AddSkill (){

    const [skills, setSkills]= useState({
        competence: "",
        information: "",
    })

    const handleChange = (e) =>{
        const {name, value }=e.target
        setSkills ((prev)=>{
            return {...prev, [name]: value}
        })}

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log(skills);
    }


    return ( 
        <div className="popup">
            <form className="addpfe" onSubmit={handleSubmit}>
                <FontAwesomeIcon icon={faXmark} className='xmark' /> <br />
                <h1>Compétence :</h1>
                <input type="text" placeholder="entrez une compétence..." name='competence' onChange={handleChange} />
                <h1>informations :</h1>
                <textarea id="textarea" type="text" placeholder="entrez des informations sur ces compétence..." name='information' onChange={handleChange} />
                <button>Ajouter</button>
            </form>
        </div>
    )
}

export default AddSkill