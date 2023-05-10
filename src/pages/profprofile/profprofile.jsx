import './profprofile.css'
import RightBar from '../../components/rightbar'
import Prfl from '../../components/prfl'
import PfeCard from '../../components/pfecard'
import AddPfe from "../../components/addpfe"
import { useState } from 'react'
import React from 'react';

function ProfProfile() {

    const [popup,setPopup] = useState(false)

    const [show,setShow] = useState(false)

    const [details, setDetails]= useState({
        name: "",
        detail: "",
        cmpt1: "",
        cmpt2: "",
        cmpt3: "",
    })

    const handleChange = (e) =>{
        const {name, value }=e.target
        setDetails ((prev)=>{
            return {...prev, [name]: value}
        })
    }

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log(details);
        console.log(details.cmpt1)
    }

    const [val,setVal]= useState([])
    const handleAdd=()=>{
        const abc=[...val,[]]
        setVal(abc)
    }

   
    const handleChangee=(onChangeValue)=>{
        const inputdata=[...val]
        const i=1
        inputdata[i]=onChangeValue.target.value;
        setVal(inputdata)
    }

    return(
        <div className="profprofile">
            <RightBar/>
            <div className="profright">
                <div className="prflprf">
                    <Prfl/>
                </div>
                <button  onClick={()=> handleAdd()}>Ajouter un PFE </button>
                {val.map((data,i)=>{
                    return(
                        <div className="pfecards">
                           <PfeCard onChange={e=>handleChangee(e,i)} details={details} setPopup={setPopup}/> 
                        </div>
                    )
                })}
                <AddPfe 
                trigger={popup} 
                setTrigger={setPopup} 
                details={details}
                handleChange={handleChange}
                handleSubmit={handleSubmit}
                show={show}
                setShow={setShow}
                />
            </div>
        </div>
    )
}

export default ProfProfile 