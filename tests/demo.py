"""
Demo script - Analytics Service Integration Test
Demonstrates that all upgraded libraries work together cohesively
"""

import numpy as np
import pandas as pd
from scipy import stats
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from datetime import datetime


def main():
    print("=" * 70)
    print("📊 ANALYTICS SERVICE - INTEGRATED DEMO")
    print("=" * 70)
    print(f"Execution time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    # 1. Generate synthetic dataset with NumPy
    print("1️⃣  GENERATING DATASET (NumPy)")
    print("-" * 70)
    np.random.seed(42)
    n_samples = 100
    
    # Create synthetic data
    data = np.random.randn(n_samples, 4) * 10 + 50
    print(f"✓ Generated {n_samples} samples with 4 features")
    print(f"  Shape: {data.shape}")
    print(f"  Mean: {data.mean():.2f}, Std: {data.std():.2f}")
    print()

    # 2. Create DataFrame with Pandas
    print("2️⃣  CREATING DATAFRAME (Pandas)")
    print("-" * 70)
    df = pd.DataFrame(
        data,
        columns=['Feature_A', 'Feature_B', 'Feature_C', 'Feature_D']
    )
    df['Category'] = np.random.choice(['Type_1', 'Type_2', 'Type_3'], n_samples)
    
    print(f"✓ DataFrame created with {len(df)} rows and {len(df.columns)} columns")
    print(f"\n{df.head()}")
    print(f"\nGroupBy summary:")
    print(df.groupby('Category')[['Feature_A', 'Feature_B']].mean())
    print()

    # 3. Statistical analysis with SciPy
    print("3️⃣  STATISTICAL ANALYSIS (SciPy)")
    print("-" * 70)
    feature_a = df['Feature_A'].values
    
    # Test normality
    statistic, p_value = stats.normaltest(feature_a)
    print(f"✓ Normality Test on Feature_A:")
    print(f"  Statistic: {statistic:.4f}, p-value: {p_value:.4f}")
    
    # Calculate percentiles
    percentiles = stats.norm.ppf([0.25, 0.5, 0.75])
    print(f"✓ Normal Distribution Percentiles (25%, 50%, 75%): {percentiles}")
    print()

    # 4. Machine Learning with scikit-learn
    print("4️⃣  DIMENSIONALITY REDUCTION (scikit-learn)")
    print("-" * 70)
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    
    pca = PCA(n_components=2)
    reduced_data = pca.fit_transform(scaled_data)
    
    print(f"✓ PCA applied (4D → 2D)")
    print(f"  Explained variance ratio: {pca.explained_variance_ratio_}")
    print(f"  Total variance explained: {sum(pca.explained_variance_ratio_):.2%}")
    print(f"  Reduced data shape: {reduced_data.shape}")
    print()

    # 5. Visualization with Matplotlib
    print("5️⃣  CREATING VISUALIZATIONS (Matplotlib)")
    print("-" * 70)
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('Analytics Service - Visualization Demo', fontsize=14, fontweight='bold')
    
    # Plot 1: Feature distribution
    axes[0, 0].hist(feature_a, bins=20, edgecolor='black', alpha=0.7, color='skyblue')
    axes[0, 0].set_title('Feature_A Distribution')
    axes[0, 0].set_xlabel('Value')
    axes[0, 0].set_ylabel('Frequency')
    
    # Plot 2: Category boxplot
    df.boxplot(column='Feature_B', by='Category', ax=axes[0, 1])
    axes[0, 1].set_title('Feature_B by Category')
    axes[0, 1].set_xlabel('Category')
    axes[0, 1].set_ylabel('Feature_B')
    
    # Plot 3: PCA scatter
    scatter = axes[1, 0].scatter(reduced_data[:, 0], reduced_data[:, 1], 
                                  c=pd.factorize(df['Category'])[0], 
                                  cmap='viridis', alpha=0.6, s=50)
    axes[1, 0].set_title('PCA Projection (2D)')
    axes[1, 0].set_xlabel(f'PC1 ({pca.explained_variance_ratio_[0]:.1%})')
    axes[1, 0].set_ylabel(f'PC2 ({pca.explained_variance_ratio_[1]:.1%})')
    
    # Plot 4: Correlation heatmap
    corr_matrix = df[['Feature_A', 'Feature_B', 'Feature_C', 'Feature_D']].corr()
    im = axes[1, 1].imshow(corr_matrix, cmap='coolwarm', aspect='auto', vmin=-1, vmax=1)
    axes[1, 1].set_title('Feature Correlation Matrix')
    axes[1, 1].set_xticks(range(4))
    axes[1, 1].set_yticks(range(4))
    axes[1, 1].set_xticklabels(['A', 'B', 'C', 'D'], rotation=45)
    axes[1, 1].set_yticklabels(['A', 'B', 'C', 'D'])
    
    plt.tight_layout()
    plt.savefig('analytics_demo_output.png', dpi=100, bbox_inches='tight')
    print(f"✓ Visualizations saved to 'analytics_demo_output.png'")
    print()

    # 6. Summary
    print("=" * 70)
    print("✅ DEMO COMPLETE - ALL LIBRARIES OPERATING NORMALLY")
    print("=" * 70)
    print()
    print("📝 Summary:")
    print(f"  ✓ NumPy:        Arrays & math operations")
    print(f"  ✓ Pandas:       Data manipulation & grouping")
    print(f"  ✓ SciPy:        Statistical analysis")
    print(f"  ✓ scikit-learn: ML & dimensionality reduction")
    print(f"  ✓ Matplotlib:   Visualization")
    print()


if __name__ == '__main__':
    main()
