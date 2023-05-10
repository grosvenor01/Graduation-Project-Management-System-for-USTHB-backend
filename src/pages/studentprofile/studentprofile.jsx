import './studentprofile.css'
import RightBar from '../../components/rightbar'
import Prfl from '../../components/prfl'
import PrflCard from '../../components/prflcard'
import React from 'react';
function StudentProfile() {
    return(
        <div className="studentprofile">
            <RightBar/>
            <div className="studentright">
                <div className="prflstd">
                    <Prfl/>
                    <div className="prflcontainer">
                    <PrflCard/>
                    <PrflCard/>
                    <PrflCard/>
                    <PrflCard/>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default StudentProfile 