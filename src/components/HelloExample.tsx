import * as React from 'react'

export interface Props {
    name: string
    enthusiasmLevel?: number
}

function getExclamationMarks(numChars: number) {
    return Array(numChars +1).join('!')
}

function HelloExample ({ name, enthusiasmLevel = 1 }: Props) {
    if (enthusiasmLevel <= 0) {
        throw new Error ('You could be a little more enthused coudln\'t you...')
    }

    return (
        <div className='hello'>
            <div className='greeting'>
                Hello {name + getExclamationMarks(enthusiasmLevel)}
            </div>
        </div>
    )
}

export default HelloExample
