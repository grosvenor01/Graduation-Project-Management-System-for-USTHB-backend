import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faXmark } from '@fortawesome/free-solid-svg-icons'
import { useState } from 'react';
import React from 'react';

function AddPfe({trigger,details,handleChange,handleSubmit,children,setTrigger,show,setShow}){

    
    return (trigger) ? (
        <div className="popup">
            <form className="addpfe" onSubmit={handleSubmit}>
            <FontAwesomeIcon icon={faXmark} className='xmark' onClick={()=> setTrigger(false)}/> <br />
            <label htmlFor="">
                Nom du PFE : <br />
                <input type="text" placeholder="entrez le nom du PFE" onChange={handleChange} name="name" />
            </label> <br />
            <label htmlFor="">
                Details du PFE : <br />
                <input type="text" placeholder="entrez les details du PFE" onChange={handleChange} name="detail" />
            </label> <br />
            <label htmlFor="">
                Competences : <br />
                <div className="cmpss">
                <input type="text" placeholder="entrez les compétence requis" onChange={handleChange}  name="cmpt1"/>
                <input type="text" placeholder="entrez les compétence requis" onChange={handleChange}  name="cmpt2" />
                <input type="text" placeholder="entrez les compétence requis"  onChange={handleChange} name="cmpt3" />
                </div>
            </label> <br />
            <button onClick={()=> setShow(true)}>Valider</button>
            {children}
           </form>
        </div>
    ) : "";
}

export default AddPfe