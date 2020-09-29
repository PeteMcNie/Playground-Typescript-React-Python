import * as constants from '../constants'

// Created two types that describe what increment actions and decrement actions should look like.
export interface IncrementEnthusiasm {
    type: constants.INCREMENT_ENTHUSIASM
}

export interface DecrementEnthusiasm {
    type: constants.DECREMENT_ENTHUSIASM
}

// Created a type (EnthusiasmAction) to describe cases where an action could be an increment or a decrement.
export type EnthusiasmAction = IncrementEnthusiasm | DecrementEnthusiasm


// Two functions that actually manufacture the actions which we can use instead of writing out bulky object literals.
export function incrementEnthusiasm(): IncrementEnthusiasm {
    return {
        type: constants.INCREMENT_ENTHUSIASM
    }
}

export function decrementEnthusiasm(): DecrementEnthusiasm {
    return {
        type: constants.DECREMENT_ENTHUSIASM
    }
}