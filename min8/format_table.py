def format_table(benchmarks, algos, results):
    column_width = []
    column_width.append(max([len(x) for x in benchmarks] + [len("Benchmark")]))
    for i in range(len(algos)):
        column_width.append(max([len(algos[i])] + [len(str(x[i]))+3 for x in results]))
    
    header = f"| {'Benchmark':<{column_width[0]}} | " + \
             " | ".join(f"{algo:<{column_width[i+1]}}" for i, algo in enumerate(algos)) + " |"
    
    separator = "-" * len(header)

    rows = []
    for i, benchmark in enumerate(benchmarks):
        row = f"| {benchmark:<{column_width[0]}} | " + \
              " | ".join(f"{results[i][j]:<{column_width[j+1]}.10f}" for j in range(len(algos))) + " |"
        rows.append(row)
    
    print(header)
    print(separator)
    for row in rows:
        print(row)