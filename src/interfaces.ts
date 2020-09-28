export interface IFootballData {
    id: number
    competition: { id: number; name: string } //area missing at this stage
    season: { id: number; startDate: string; endDate: string; currentMatchday: number; winner: null }
    utcDate: string
    status: string
    matchday: number
    stage: string
    group: string
    lastUpdated: string
    odds: { msg: string }
    score: { winner: null; duration: string; fullTime: object; halfTime: object; extraTime: object; penalties: object }
    homeTeam: { id: number; name: string }
    awayTeam: { id: number; name: string }
    referees: Array<T>;
}