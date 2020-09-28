import React, { useState } from 'react'

export interface Props {
    name: string
    enthusiasmLevel?: number
}

interface IEnthusiasm {
    currentEnthusiasm: number
}

function StateHello (props: Props) {
    let [currentEnthusiasm, setCurrentEnthusiasm] = useState<number>(1)

    return (
        <div className='helloExample'>
            <div className='greeting'>
                Hello {props.name + getExclamationMarks(currentEnthusiasm)}
            </div>
            <button onClick={() => setCurrentEnthusiasm(currentEnthusiasm--)}>-</button>
            <button onClick={() => setCurrentEnthusiasm(currentEnthusiasm++)}>+</button>
        </div>
    )
}

export default StateHello


function getExclamationMarks (numChars: number) {
    return Array(numChars + 1).join('!')
}
