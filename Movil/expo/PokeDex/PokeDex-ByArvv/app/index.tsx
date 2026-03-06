import {useState, useEffect} from 'react'
import {View} from 'react-native'
import PokemonCard from '@/components/pokemonCard'

export default function index () {

  const[pokeData, setPokeData] = useState()
  const pokemon_URL = 'https://pokeapi.co/api/v2/pokemon/'

  const fetchPokemon = async (identifier : String | number) => {
    try {
      const response = await fetch(`${pokemon_URL}${identifier}`)
      const data = await response.json()
      setPokeData(data)
    } catch (error) {
      console.error('El fetch no se a podido completar')
    }
  }

  useEffect(() =>{
    fetchPokemon('snorunt')
  },[] )

  return (
    <View>
      <PokemonCard pokeData={pokeData}/>
    </View>
  )
}