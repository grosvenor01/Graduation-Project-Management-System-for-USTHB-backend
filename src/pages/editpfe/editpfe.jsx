import './editpfe.css'
import { useState, useEffect } from 'react'
import {useNavigate} from 'react-router-dom'
import React from 'react';
function EditPfe() {

     const [infos, setInfos]= useState({
       niveau:"",
       nom1:"",
       nom2:"",
       nom1_matricule:"",
       nom2_matricule:"",
       nom1_tel:"",
       nom2_tel:"",
       nom2_email:"",
       nom1_email:"",
       nom1_encadreur:"",
       nom2_encadreur:null,
       nom1_encemail:"",
       nom2_encemail:null,
       titre:"",
       mot_cle:"",
       plan:"",
       raison_social:"",
       choix:"",
       organisme:"",
       raison_social:"",
       nom1_encGrade:"",
       nom2_encGrade:null,
       gl:"Off",
       reseau:"Off",
       ai:"Off",
       web:"Off",
       info_th:"Off",
       BioInfo:"Off",
       archi:"Off",
       computer_vision:"Off",
     })

    const handleChange = (e) =>{
       const {name, value }=e.target
       setInfos ((prev)=>{
        return {...prev, [name]: value}
    })}

    const history = useNavigate()

   const handleSubmit = async(e) => {
      e.preventDefault();
      console.log(infos);
      const response = await fetch("http://localhost:8000/api/envoyer-fiche-de-pfe/",{
        method: "POST",
        headers: {
            'Content-Type' : 'application/json',
        },
        body: JSON.stringify(infos)
      })
      const result = await response.json();
      console.log(result)
      history("/home")
   }

    return (
        <form className="pfe" onSubmit={handleSubmit}>
            <h1>Information de PFE</h1>
            <p>Remplissez ce formulaire pour  generer une fiche de pfe   </p>

            <div className="formpfe">
              <div className="Pleft">

                <p>Interessé par </p>
                  <label htmlFor=""  >
                    <input type="radio" name='gl' className='choix'  onChange={handleChange} value="oui" />
                    Génie logeciel
                  </label>

        
                  <label htmlFor="">
                    <input type="radio"  name='reseau' className='choix' onChange={handleChange} value="oui"/>
                    Réseaux
                  </label>


                  <label htmlFor="">
                    <input type="radio"  name='ai' className='choix' onChange={handleChange} value="oui"/>
                    Intiligence Artificiel
                  </label>
                  <br/>

                  
                  <label htmlFor="">
                    <input type="radio"  name='archi' className='choix' onChange={handleChange} value="oui"/>
                    Architecture des PCs
                  </label>


                  <label htmlFor="">
                    <input type="radio" name='computer_vision' className='choix' onChange={handleChange} value="oui" />
                    Informatique visuelle
                  </label>


                  <label htmlFor="">
                    <input type="radio" name='info_th' className='choix' onChange={handleChange} value="oui" />
                    Informatique théorique 
                  </label>
                  <br/>


                  <label htmlFor="">
                    <input type="radio" name='web' className='choix' onChange={handleChange} value="oui"/>
                    Web devloppment et application devloppment
                  </label>


                  <label htmlFor="">
                    <input type="radio"  name='BioInfo' className='choix' onChange={handleChange} value="oui"/>
                    Bio Informatique
                  </label>


                   <p>Niveau</p>
                  <label htmlFor="">
                    
                    <select name="niveau" id="" onChange={handleChange} >
                        
                        <option value="L3">l3</option>
                        <option value="M2">M2</option>    
                    </select>
                  </label> <br />

                  <label htmlFor="">
                  <p>Nom etudiant 1</p> 
                  <input type="text" className='inputp' placeholder='Entrez le nom ' name='nom1' onChange={handleChange}/>
                  </label> <br />

                  <label htmlFor="">
                  <p>Email etudiant 1</p> 
                  <input type="text" className='inputp' placeholder='Entrez email' name='nom1_email' onChange={handleChange}/>
                  </label> <br />

                  <label htmlFor="">
                  <p>Nom etudiant 2</p> 
                  <input type="text" className='inputp' placeholder='Entrez le nom ' name='nom2' onChange={handleChange}/>
                  </label> <br />

                  <label htmlFor="">
                  <p>Email etudiant 2 </p>
                  <input type="text" className='inputp' placeholder='Entrez email' name='nom2_email' onChange={handleChange} />
                  </label> <br />

                  <label htmlFor="">
                  <p>Nom encadreur</p> 
                  <input type="text" className='inputp' placeholder='Entrez le nom encadreur' name='nom1_encadreur' onChange={handleChange} />
                  </label> <br />

                  <label htmlFor="">
                  <p>Email encadreur</p> 
                  <input type="text" className='inputp' placeholder='Entrez email' name='nom1_encemail' onChange={handleChange} />
                  </label> <br />

                  <label htmlFor="">
                  <p>Titre de projet</p> 
                  <input type="text" className='inputp' placeholder='Entrez le ttire du projet' name='titre' onChange={handleChange} />
                  </label> <br />

                  <label htmlFor="">
                  <p>mot clé</p>  
                  <input type="text" className='inputp' placeholder='Entrez le mot clé' name='mot_cle'  onChange={handleChange}/>
                  </label> <br />

                  <label htmlFor="">
                    <p>Plan de travail</p> 
                    <textarea  name='plan' onChange={handleChange} ></textarea>
                  </label> <br />

                </div>



                <div className="Pright">
                <label htmlFor="">
                    <p>Specialité</p> 
                    <select name="choix" id="" defaultValue={2} onChange={handleChange}>
                        <option value="ACAD">ACAD</option>
                        <option value="ISIL">ISIL</option>
                        <option value="GTR">GTR</option>
                        <option value="4">SII</option>
                        <option value="5">SII</option>
                        <option value="6">IV</option>
                        <option value="7">IL</option>
                        <option value="8">BIOINFO</option>
                        <option value="9">BIGDATA</option>
                    </select>
                  </label> <br />

                  <label htmlFor="">
                  <p>organisme</p> 
                    <select name="organisme" id="" onChange={handleChange}>
                        
                        <option value="1">interne</option>
                        <option value="2">externe</option>
                    </select>
                  </label> <br /> <br /> <br /> <br /> <br /> <br />

                  <label htmlFor="">
                  <p>Matricule etudiant 1</p>  
                  <input type="text" className='inputp' placeholder='Entrez la matricule' name='nom1_matricule' onChange={handleChange} />
                  </label> <br />

                  <label htmlFor="">
                  <p>numero etudiant 1</p>  
                  <input type="text" className='inputp' placeholder='Entrez le numéro de téléphone' name='nom1_tel' onChange={handleChange} />
                  </label> <br />

                  <label htmlFor="">
                  <p>Matricule etudiant 2</p>  
                  <input type="text" className='inputp' placeholder='Entrez la matricule' name='nom2_matricule' onChange={handleChange} />
                  </label> <br />

                  <label htmlFor="">
                  <p>numero etudiant 2</p> 
                  <input type="text" className='inputp' placeholder='Entrez le numéro de téléphone' name='nom2_tel' onChange={handleChange}/>
                  </label> <br />

                  <label htmlFor="">
                  <p>grade encadreur </p> 
                  <input type="text" className='inputp' placeholder='Entrez le grade ' name='nom1_encGrade' onChange={handleChange} />
                  </label> <br />

                  <label htmlFor="">
                    <p>résumé du projet</p>  <br /> 
                    <textarea className='resumé' name='resume' onChange={handleChange}></textarea>
                  </label> <br />

                  <label htmlFor="">
                  <p>service</p>  
                  <input type="text" className='inputp' placeholder='Entrez le service ' name="service" onChange={handleChange}/>
                  </label> <br />

                  <label htmlFor="">
                  <p>raison social</p>  
                  <input type="text" className='inputp' placeholder='Entrez la raison social ' name='raison_social' onChange={handleChange} />
                  </label> <br />

                </div>

            </div>
            <div className='buttonsp'>
                    <button className='btnn1'>Ajouter  les informations </button>
                    <button className='btnn2'>Aide d’utilisation </button>
            </div>
        </form>
    )
}

export default EditPfe