import * as React from 'react'

export interface Props {
    name: string
    enthusiasmLevel?: number
    onIncrement?: () => void
    onDecrement?: () => void
}

function getExclamationMarks(numChars: number) {
    return Array(numChars +1).join('!')
}

function HelloExample ({ name, enthusiasmLevel = 1, onIncrement, onDecrement }: Props) {
    if (enthusiasmLevel <= 0) {
        throw new Error ('You could be a little more enthused coudln\'t you...')
    }

    return (
        <div className='hello'>
            <div className='greeting'>
                Hello {name + getExclamationMarks(enthusiasmLevel)}
            </div>
            <div>
                <button onClick={onDecrement}>-</button>
                <button onClick={onIncrement}>+</button>
            </div>
        </div>
    )
}

export default HelloExample
