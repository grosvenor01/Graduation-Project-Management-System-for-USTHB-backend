import usthb from '../assets/images/usthb.png';
import React from 'react';
function Footer(){
    return(
        <div className='footer'>
            <h1 className='footertitle'>Commancer ou Encadrer <br /> votre PFE au plus tot <br /> possible.</h1>
            <div className='buttons'>
                <a href="/login"><button className='btn1'>Get started</button></a>
                <button className='btn2'>contact us</button>
            </div>
          

        </div>
    )
}

export default Footer