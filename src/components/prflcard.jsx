import { useState } from "react"
import Circularprogress from "./circularprogress"
import React from 'react';
function PrflCard() {

    const [persentage,setPersentage]= useState(10)

    return <div className="prflcard">
        <h1>Skill</h1>
        <div className="circular">
            <Circularprogress persentage={persentage} circleWidth="200"/>
            <input 
            className="circular-input"
            type="range"
            min='1' 
            max='100'
            step='1' 
            value={persentage} 
            onChange={(ev)=> setPersentage(ev.target.value)}
        />
        </div>
        <h3>info</h3>
        <h4>Lorem ipsum dolor sit amet, <br />
            consectetur adipiscing elit, sed do <br />
            eiusmod tempor incididunt </h4>
    </div>
}

export default PrflCard