import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faImage,  faFilePdf } from '@fortawesome/free-solid-svg-icons'
import { useState, useEffect } from 'react'
import {useNavigate} from 'react-router-dom'
import React from 'react';
function EditProfP(){

   const [infos, setInfos]= useState({
      user:1,
      speciality: "",
      grade: "",
      university_name: "",
      cv:null,
      rating:5,
      themes_proposed:null
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
      const response = await fetch("http://localhost:8000/api/ensignant_profile/",{
          method: "POST",
          headers: {
              'Content-Type' : 'application/json',
          },
          body: JSON.stringify(infos)
      })
      const result = await response.json();
      console.log(result)
      history("/profprofile")
  }


    return(
        <div className='editstudent'>
            <h1>Information de profile</h1>
            <p>Remplissez ce formulaire pour accéder à la page principale </p>
            
            <form action="" className='form' onSubmit={handleSubmit}>
               <p className='firstp'>Photo de profile</p>
               <div className='img'>
                  <FontAwesomeIcon icon={faImage} className='image'/>  
                  <p>deposer votre photo de profile ici. Max size : 2MB</p>
                  <input type="file" className='inputp' placeholder='Entrer le CV' name='profil_pic'/>
               </div>
               <div className='top'>
                  <label htmlFor="">
                  université <br />
                  <input type="text" className='inputp' placeholder='Entrer le nom de votre université'  name='university_name' onChange={handleChange} />
                  </label> <br />

                  <label htmlFor="" >
                  <span>specialité </span> <br />
                  <input type="text" className='inputp marge'  placeholder='Entrer le nom de votre Specialité' name='speciality' onChange={handleChange}/>
                  </label>
                  <br />
               </div>

                <br /> <br />
               <label htmlFor="">
                <span className='textprof'>grade</span> <br />
                  <input type="text" className='inputp' placeholder='MDN' name="grade" onChange={handleChange} />
                  </label> <br />

               <div className='buttonsp'>
                <button className='btnn1'>Ajouter  les informations </button>
                <button className='btnn2'>Aide d’utilisation </button>
               </div>
            </form>
        </div>
    )
}

export default EditProfP