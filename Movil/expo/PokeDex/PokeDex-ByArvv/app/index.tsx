import {useState, useEffect} from 'react'
import { router } from 'expo-router'
import {View, Pressable} from 'react-native'
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
      <Pressable onPress={() => router.push("/new-screen")}></Pressable>
      <PokemonCard pokeData={pokeData}/>
    </View>
  )
}