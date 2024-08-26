import { useQuery } from '@tanstack/react-query'
import { useCallback } from 'react'
import { Configuration, RecipesApi } from '../api/generated'
import { API_BASE_URL } from '../App'


export const useGetRecipe = (recipeId: string) => {
    const config: Configuration = {
        basePath: API_BASE_URL,
        isJsonMime: () => {
            return true
        },
    }
    const recipeAPI = new RecipesApi(config)

    const getRecipe = useCallback(async (recipeId: string) => {
        return await recipeAPI
            .getOneRecipesIdGet(recipeId)
            .then((response) => {
                return response.data
            })
            .catch((error) => {
                throw error
            })
    }, [])

    const { data: recipe, isLoading: isLoadingRecipe } = useQuery({
        queryKey: ['allRecipes'],
        queryFn: () => getRecipe(recipeId),
    })

    return { recipe, isLoadingRecipe }
}
