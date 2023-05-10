import time from '../assets/images/Delivery Time.svg';
import send from '../assets/images/Email Send.svg';
import message from '../assets/images/Hint.svg';
import React from 'react';
function Info(){
    return(
        <div className="info">
           <h1 className='info-title'>
           le moyen le plus <br />
           simple de démarrer <br /> 
           votre PFE.
           </h1>
           <div className='info2'>
              <div className='info2-div'>
                <img className='icon' src={message} alt="" />
                <h2>Recommander <br />
                des theme</h2>
                <p>la platforme contient <br /> plus de 100 themes <br /> proposé chaque année</p>
              </div>
              <div className='info2-div'>
                <img className='icon' src={send} alt="" />
                <h2>Simplifier la <br />
                communication</h2>
                <p>cette platforme est la <br /> meilleur method pour <br /> contacter un ensignant <br /> dans le departement </p>
              </div>
              <div className='info2-div'>
                <img className='icon' src={time} alt="" />
                <h2>réduction du <br />
                temps perdu</h2>
                <p>on est travailler pour <br /> reduire le temp perdu <br /> sur cette processus le <br /> maximum </p>
              </div>
           </div>
        </div>
    )
}

export default Info 