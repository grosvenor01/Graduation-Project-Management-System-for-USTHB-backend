import image1 from '../assets/images/image1.png';
import image2 from '../assets/images/image2.png';
import image3 from '../assets/images/image3.png';
import image4 from '../assets/images/image4.png';
import React from 'react';

function Photos(){
    return(
        <div className="photos">
          <div className='div1'>
            <h1 className='title-div1'>
            Avoir plus de temp <br /> pour un projet plus <br /> 
            professionel
            </h1>
            <button className='div1-button'>s'inscrire</button>
          </div>

          <div className='div2'>
            <div>
            <img src={image1} alt="" />
            <img src={image2} alt="" />
            </div>
            <div>
            <img src={image3} alt="" />
            <img src={image4} alt="" />
            </div>
          </div>
        </div>
    )
}

export default Photos