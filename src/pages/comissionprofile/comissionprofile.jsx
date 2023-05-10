import './comissionprofile.css'
import RightBar from '../../components/rightbar'
import Prfl from '../../components/prfl'
import CommiCard from '../../components/commicard'
import React from 'react';
function CommissionProfile(){
    return (
        <div className="commision">
            <RightBar/>
            <div className="resporight">
            <Prfl/>
            <h1>Themes a valider</h1>
            <div className="repocards">
                <CommiCard />
                <CommiCard />
                <CommiCard />
                <CommiCard />
            </div>
         </div>
        </div>
    )
}

export default CommissionProfile