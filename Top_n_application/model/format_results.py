def format_results(results_list):
    """Will format the results list into a dictonary to be printed by front
    end with indices being replaced by genres and decimals converted to
    percentages."""
    MAP_MATCHING = {0: 'Classical', 1: 'Blues', 2: 'Country',
                    3: 'Disco', 4: 'Hip Hop', 5: 'Jazz', 6: 'Metal',
                    7: 'Pop', 8: 'Reggae', 9: 'Rock'}
    results = [round(x*100, 2) for x in results_list]
    sorted_results = {}
    for i in range(0, len(results_list)):
        sorted_results[MAP_MATCHING[i]] = results[i]
    sorted_results = sorted(sorted_results.items(),
                            key=lambda x: x[1],
                            reverse=True)
    final_results_dict = dict(sorted_results)
    return final_results_dict


if __name__ == "__main__":
    pass
