import './editstudentp.css'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faImage,  faFilePdf } from '@fortawesome/free-solid-svg-icons'
import { useState, useEffect } from 'react'
import {useNavigate} from 'react-router-dom'
import React from 'react';
function EditStudentP(){
 

   const [infos, setInfos]= useState({
      user:1,
      speciality: "",
      interested: "",
      university_name: "",
      CV: null,
      study_level: "", 
      github_link: "",
      linkedin_link: "",
      binome: "",
      Role:""
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
      const response = await fetch("http://localhost:8000/api/student_profile/",{
          method: "POST",
          headers: {
              'Content-Type' : 'application/json',
          },
          body: JSON.stringify(infos)
      })
      const result = await response.json();
      console.log(result)
      history("/studentprofile")
  }




    return(
        <div className='editstudent'>
            <h1>Information de profile</h1>
            <p>Remplissez ce formulaire pour accéder à la page principale </p>
            
            <form action="" className='form' onSubmit={handleSubmit}>
               <p className='firstp'>Photo de profile</p>
               <div className='img'  >
                  <FontAwesomeIcon icon={faImage} className='image'/>  
                  <p>deposer votre photo de profile ici. Max size : 2MB</p>
                  <input type="file" className='inputp' placeholder='Entrer le CV' name='profil_pic'/>
               </div>

               <p>CV</p>
               <div className='pdf' name="CV" >
                  <FontAwesomeIcon icon={faFilePdf} className='image'/>
                  <p>deposer votre CV ici. Max size : 10MB ..</p>
                  <input type="file" className='inputp' placeholder='Entrer le CV' name='CV'/>
               </div>

               <div className='top'>
                  <label htmlFor="">
                  université <br />
                  <input type="text" className='inputp' placeholder='Entrer le nom de votre université' name='university_name'   onChange={handleChange}/>
                  </label> <br />

                  <label htmlFor="" >
                  <span>specialité </span> <br />
                  <input type="text" className='inputp marge'  placeholder='Entrer le nom de votre Specialité' name='speciality'  onChange={handleChange}/>
                  </label>
                  <br />
               </div>

               <div className='bottom'>
                  <label htmlFor="">
                  Lien vers github <br />
                  <input type="text" className='inputp'  placeholder='www.github.com/username' name='github_link'  onChange={handleChange} />
                  </label>
                  <br />

                  <label htmlFor="">
                  <span>Lien vers linkedin</span> <br />
                  <input type="text" className='inputp marge'  placeholder='www.linkedin.com/username'  name='linkedin_link'  onChange={handleChange}/> 
                  </label>
                  <br />
               </div>

               <div className='bottom'>
                    <label htmlFor="">
                      Role <br/>
                        <select name="Role" className='inputp' id="" onChange={handleChange}  >
                           <option value="monome">monome</option>
                           <option value="Binome">Binome</option>
                        </select>
                    </label>
                  <br />

                  <label htmlFor="">
                    <span>study level </span><br/>
                    <select name="study_level" className='inputp marge' id=""  onChange={handleChange} >
                        <option value="L3">L3</option>
                        <option value="M2">M2</option>
                    </select>
                  </label>
                  <br />
               </div>
  
               <p className='textareap'>A propos</p>
               <label htmlFor="">
                    <textarea name="interested" id="" cols="30" rows="10" placeholder='Bio '   onChange={handleChange} ></textarea>
                </label>

               <p className='textareap'  >tager  votre binome</p>
               <input type="text" placeholder='his email here ' className='inputp inputpp' name='binome'  onChange={handleChange}/>

               <div className='buttonsp'>
                <button className='btnn1'>Ajouter  les informations </button>
                <button className='btnn2'>Aide d’utilisation </button>
               </div>
            </form>
        </div>
    )
}

export default EditStudentP